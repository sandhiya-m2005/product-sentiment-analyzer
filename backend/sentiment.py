import { Pie } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from 'chart.js'

ChartJS.register(ArcElement, Tooltip, Legend)

const SentimentChart = ({ data }) => {
  const counts = { positive: 0, negative: 0, neutral: 0 }
  data.forEach(d => counts[d.sentiment]++)

  return (
    <Pie
      data={{
        labels: ['Positive', 'Negative', 'Neutral'],
        datasets: [
          {
            data: [counts.positive, counts.negative, counts.neutral]
          }
        ]
      }}
    />
  )
}

export default SentimentChart
```jsx
import { Pie } from 'react-chartjs-2'

const SentimentChart = ({ data }) => {
  const counts = { positive: 0, negative: 0, neutral: 0 }
  data.forEach(d => counts[d.sentiment]++)

  return (
    <Pie data={{
      labels: ['Positive', 'Negative', 'Neutral'],
      datasets: [{
        data: [counts.positive, counts.negative, counts.neutral]
      }]
    }} />
  )
}

export default SentimentChart
frontend/src/styles/App.css
.app {
  text-align: center;
  padding: 20px;
}
input {
  padding: 8px;
  width: 300px;
}
button {
  margin-left: 10px;
  padding: 8px 15px;
}