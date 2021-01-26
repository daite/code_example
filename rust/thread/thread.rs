#[macro_use] extern crate prettytable;
use prettytable::{Table, Row, Cell};
use prettytable::format;

use select::document::Document;
use select::predicate::{Predicate, Attr, Name};
use std::error::Error;
use reqwest;

use std::sync::{Mutex, Arc};
use std::thread;


fn main() {

    let mut bbs_urls = vec![];
    let mut titles = vec![];

    let play_url = "http://zhuixinfan.com/viewtvplay-1076.html";
    let body = reqwest::blocking::get(play_url).unwrap().text().unwrap();
    let doc = Document::from(&body[..]);
    for elem in doc.find(Attr("class", "td2").descendant(Name("a"))) {
        titles.push(elem.text());
        let bbs_url = format!("{}{}", "http://zhuixinfan.com/", elem.attr("href").unwrap());
        bbs_urls.push(bbs_url);
    }
    
    let vec = Arc::new(Mutex::new(Vec::new()));
    let mut handles = vec![];

    for (title, url) in titles.into_iter().zip(bbs_urls.into_iter()) {    
        let vec = Arc::clone(&vec);
        let handle = thread::spawn(move || {
            let a = get_magnet(&url);
            let mut m = vec.lock().unwrap();
            (*m).push((title, a));
        });
        handles.push(handle);
    }
    for h in handles {
        h.join().unwrap();
    }
    let final_data = &mut *vec.lock().unwrap();
    final_data.sort();
    let mut table = Table::new();
    table.set_titles(row!["TITLE", "MAGNET"]);
    for (t, m) in final_data {
        table.add_row(Row::new(vec![
            Cell::new(&t),
            Cell::new(&m),
        ]));
    }
    table.set_format(*format::consts::FORMAT_NO_LINESEP_WITH_TITLE);
    table.printstd();
}

fn run() -> Result<(), Box<dyn Error>> {
    let mut titles = vec![];
    let mut magnets = vec![];
    let url = "http://zhuixinfan.com/viewtvplay-1076.html";
    let body = reqwest::blocking::get(url)?.text()?;
    let doc = Document::from(&body[..]);
    for elem in doc.find(Attr("class", "td2").descendant(Name("a"))) {
        titles.push(elem.text());
        let bbs_url = format!("{}{}", "http://zhuixinfan.com/", elem.attr("href").unwrap());
        magnets.push(get_magnet(&bbs_url[..]))
    }

    let mut table = Table::new();
    table.set_titles(row!["TITLE", "MAGNET"]);
    for (t, m) in titles.iter().zip(magnets.iter()) {
        table.add_row(Row::new(vec![
            Cell::new(t),
            Cell::new(m),
        ]));
    }
    table.set_format(*format::consts::FORMAT_NO_LINESEP_WITH_TITLE);
    table.printstd();

    Ok(())
}


fn get_magnet(bbs_url: &str) -> String {
    let body = reqwest::blocking::get(bbs_url).unwrap().text().unwrap();
    let doc = Document::from(&body[..]);
    let d = doc.find(Attr("id", "torrent_url")).next().unwrap().text();
    let magnet = d.split("&").collect::<Vec<&str>>()[0];
    String::from(magnet)
}