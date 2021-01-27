package main

// #cgo CFLAGS: -I${SRCDIR}/callClib
// #cgo LDFLAGS: ${SRCDIR}/callC.a
// #include <stdlib.h>
// #include <callC.h>
import "C"
import (
	"fmt"
	"unsafe"
)

func main() {
	fmt.Println("Going to call C function")
	C.cHello()
	m := C.CString("This is chris")
	defer C.free(unsafe.Pointer(m))
	C.printMessage(m)
	fmt.Println("All perfect done!")
}
