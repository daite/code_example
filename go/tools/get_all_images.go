package main

import (
	"crypto/md5"
	"fmt"
	"github.com/PuerkitoBio/goquery"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"sync"
)

var (
	saveDir   = ""
	wg        sync.WaitGroup
	userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
)

func init() {
	curDir, _ := os.Getwd()
	saveDir = filepath.Join(curDir, "images")
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("[Usage] ./get_all_images <url>")
		os.Exit(-1)
	}

	targetUrl := os.Args[1]
	resp, err := getResponseFromUrl(targetUrl)
	if err != nil {
		fmt.Printf("[-] unable to reach to %s\n", targetUrl)
		return
	}
	defer resp.Body.Close()

	doc, err := goquery.NewDocumentFromResponse(resp)
	if err != nil {
		fmt.Println(err)
	}

	saveDir = filepath.Join(saveDir, getHashVal(targetUrl))
	var imageUrls []string
	imageUrls = gatherImageUrls(doc, "img", "src", imageUrls)
	imageUrls = gatherImageUrls(doc, "a", "href", imageUrls)

	for _, imageUrl := range imageUrls {
		wg.Add(1)
		go func(imageUrl string) {
			defer wg.Done()
			downloadImageFromUrl(imageUrl)
		}(imageUrl)
	}
	wg.Wait()
}

func getResponseFromUrl(url string) (resp *http.Response, err error) {
	client := &http.Client{}
	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Add("User-Agent", userAgent)
	resp, err = client.Do(req)
	return
}

func downloadImageFromUrl(url string) {
	resp, err := getResponseFromUrl(url)
	if err != nil {
		fmt.Printf("[-] unable to reach to %s\n", url)
		return
	}
	defer resp.Body.Close()

	fmt.Printf("[+] Downloding image from %s\n", url)
	fileName := getFileNameFromUrl(url)
	if _, err := os.Stat(saveDir); err != nil {
		os.MkdirAll(saveDir, 0777)
	}
	filePath := filepath.Join(saveDir, fileName)
	f, err := os.Create(filePath)
	if err != nil {
		fmt.Println(err)
	}
	io.Copy(f, resp.Body)
}

//get hash value
func getHashVal(str string) (hashVal string) {
	data := []byte(str)
	hashVal = fmt.Sprintf("%x", md5.Sum(data))
	return
}

//find image url by using tag & attr
func gatherImageUrls(doc *goquery.Document, tag string, attr string, imageUrls []string) []string {
	doc.Find(tag).Each(func(i int, s *goquery.Selection) {
		if url, ok := s.Attr(attr); ok {
			if checkImageExtension(url) {
				imageUrls = append(imageUrls, url)
			}
		}
	})
	return imageUrls
}

//get file name from url
func getFileNameFromUrl(url string) string {
	hashVal := getHashVal(url)
	stringSlice := strings.Split(url, ".")
	stringSliceLength := len(stringSlice)
	return hashVal + "." + stringSlice[stringSliceLength-1]
}

//check image file extension
func checkImageExtension(url string) bool {
	imageExtension := []string{
		".jpeg", ".jpg", ".gif", ".png",
	}
	for _, imgExt := range imageExtension {
		if strings.HasSuffix(url, imgExt) {
			return true
		}
	}
	return false
}
