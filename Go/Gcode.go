package main

import (
    "fmt"
    "os"
    "path/filepath"
    "time"
    "strconv"
)

func main() {
    A := []int{16, 85, 60, /* ... */ }

    // Hace que el archivo se cree en la misma carpeta del código
    directorio, err := filepath.Abs(filepath.Dir(os.Args[0]))
    if err != nil {
        fmt.Println("Error al obtener el directorio:", err)
        return
    }
    archivo := filepath.Join(directorio, "resultado_go.txt")

    inicio := time.Now()

    for i := 0; i < len(A)-1; i++ {
        for j := 0; j < len(A)-1-i; j++ {
            if A[j] > A[j+1] {
                A[j], A[j+1] = A[j+1], A[j]
            }
        }
    }

    fin := time.Now()
    tiempo := fin.Sub(inicio).Milliseconds()

    file, err := os.Create(archivo)
    if err != nil {
        fmt.Println("Error al crear el archivo:", err)
        return
    }
    defer file.Close()

    for _, v := range A {
        _, err = file.WriteString(fmt.Sprintf("%d,", v))
        if err != nil {
            fmt.Println("Error al escribir en el archivo:", err)
            return
        }
    }

    fmt.Println("Go: "+strconv.FormatFloat(tiempo, 'f', -1, 64)+"ms")
}
