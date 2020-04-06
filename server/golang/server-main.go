package main

import (
  "fmt"
  "log"
  "net/http"
)

func hello(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, "hello\n")
}

func get_next_task_payload(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, "next task payload\n")
}

func main() {
  log.Print("main called")
  http.HandleFunc("/hello", hello)
  http.HandleFunc("/task/encryption/next", get_next_task_payload)

  log.Print("main running listen and serve on port 8090")
  http.ListenAndServe(":8090", nil)
}
