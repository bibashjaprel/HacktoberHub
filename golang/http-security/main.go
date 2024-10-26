
package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"
)

// list of important security headers to check
var securityHeaders = []string{
	"Content-Security-Policy",
	"X-Content-Type-Options",
	"X-Frame-Options",
	"X-XSS-Protection",
	"Strict-Transport-Security",
	"Referrer-Policy",
	"Permissions-Policy",
}

func main() {
	url := flag.String("url", "", "URL to check for security headers")
	flag.Parse()

	if *url == "" {
		fmt.Println("Usage: go run main.go -url=https://example.com")
		os.Exit(1)
	}

	resp, err := http.Get(*url)
	if err != nil {
		log.Fatalf("Failed to fetch headers: %v", err)
	}
	defer resp.Body.Close()

	fmt.Printf("Checking security headers for: %s\n\n", *url)

	checkHeaders(resp.Header)
}

func checkHeaders(headers http.Header) {
	for _, header := range securityHeaders {
		if value := headers.Get(header); value != "" {
			fmt.Printf("[+] %s: Found (Value: %s)\n", header, value)
		} else {
			fmt.Printf("[-] %s: Missing\n", header)
		}
	}
}
