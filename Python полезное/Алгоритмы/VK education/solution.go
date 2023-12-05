package main

import (
    "fmt"
    "sort"
)

func three(arr []int) int {
    m := len(arr)
    h := make([]int, m)
    copy(h, arr)
    sort.Ints(h)
    res := h[0]
    return res
}

func main() {
    var kal int
    fmt.Scan(&kal)
    mass := make([]int, kal)
    for i := 0; i < kal; i++ {
        fmt.Scan(&mass[i])
    }
    fmt.Println(three(mass))
}