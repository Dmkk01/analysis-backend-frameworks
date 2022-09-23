package main

import (
	"log"
	"os"
	"math/big"
	"github.com/gin-gonic/gin"
	_ "github.com/heroku/x/hmetrics/onload"
)

type message struct {
    Message     string  `json:"message"`
}

func main() {
	port := os.Getenv("PORT")

	if port == "" {
		log.Fatal("$PORT must be set")
	}

	router := gin.New()
	router.Use(gin.Logger())

	router.GET("/", func(c *gin.Context) {
		check := message{Message:"Health check"}
		c.JSON(200, &check)
	})

	router.GET("/hello", func(c *gin.Context) {
		hello := message{Message:"Hello World"}
		c.JSON(200, hello)
	})

	router.GET("/fibonacci", func(c *gin.Context) {
		numbers := make(map[int] string)
		n1 := big.NewInt(0)
		n2 := big.NewInt(1)
		nextTerm := big.NewInt(1)
		for i := 1; i < 1001; i++ {
			nextTerm.Add(n1, n2)
			n1 = n2
			n2 = nextTerm
			numbers[i] = n1.Text(10)
		}
		c.JSON(200, numbers)
	})

	router.Run(":" + port)
}
