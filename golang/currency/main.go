// Currency conversion program in golang 
// Author: @codedsprit <roshan0x01@gmail.com>
// Date: Oct 26 2024

package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)
// apt from https://www.exchangerate-api.com/
const apiURL = "https://api.exchangerate-api.com/v4/latest/USD"

// ExchangeRates struct to hold the response from the API
type ExchangeRates struct {
	Rates map[string]float64 `json:"rates"`
}

func getExchangeRates() (map[string]float64, error) {
	resp, err := http.Get(apiURL)
	if err != nil {
		return nil, fmt.Errorf("failed to fetch exchange rates: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("API error: %s", resp.Status)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("failed to read response: %v", err)
	}

	var rates ExchangeRates
	if err := json.Unmarshal(body, &rates); err != nil {
		return nil, fmt.Errorf("failed to parse response: %v", err)
	}

	return rates.Rates, nil
}

func convertCurrency(amount float64, from string, to string, rates map[string]float64) (float64, error) {
	fromRate, fromExists := rates[from]
	toRate, toExists := rates[to]

	if !fromExists || !toExists {
		return 0, fmt.Errorf("invalid currency code(s): from=%s, to=%s", from, to)
	}

// conversion formula
	convertedAmount := amount * (toRate / fromRate)
	return convertedAmount, nil
}

func main() {
	var amount float64
	var fromCurrency, toCurrency string

// fetch exchange rates
	rates, err := getExchangeRates()
	if err != nil {
		fmt.Println(err)
		return
	}

// provide inputs 
	fmt.Print("Enter the amount: ")
	fmt.Scan(&amount)
	fmt.Print("From currency (e.g., USD, EUR): ")
	fmt.Scan(&fromCurrency)
	fmt.Print("To currency (e.g., USD, EUR): ")
	fmt.Scan(&toCurrency)
	convertedAmount, err := convertCurrency(amount, fromCurrency, toCurrency, rates)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Printf("%.2f %s = %.2f %s\n", amount, fromCurrency, convertedAmount, toCurrency)
}

