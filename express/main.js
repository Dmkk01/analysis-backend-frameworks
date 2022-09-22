const express = require('express');

const app = express();

const PORT = process.env.PORT || 3055

app.use(express.json())

app.get('/', (req, res) => {
  res.send('Health check');
});

const getFibonacciList = () => {
  const numbers = {}
  let n1 = 0
  let n2 = 1
  let nextTerm

  for (let i=1; i <= 1000; i++) {
    nextTerm = n1 + n2
    n1 = n2
    n2 = nextTerm
    numbers[i] = n1
  }

  return numbers
}

app.get('/fibonacci', (req, res) => {
  const fibonacci = getFibonacciList()
  res.json(fibonacci)
})

app.get('/hello', (req, res) => {
  res.json({message: 'Hello World'});
});

app.listen(PORT, () => console.log(`App is listening on port ${PORT}. \n http://localhost:3055/`));