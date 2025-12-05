// Valuation/funding snapshot with citations.
// Figures are from the Research briefing; keep numbers in USD where possible.
window.fundingData = {
  labels: ['OpenAI', 'Anthropic', 'Microsoft', 'Alphabet (Google)', 'Meta', 'Mistral'],
  datasets: [
    {
      label: 'Valuation / Market Cap (USD billions)',
      data: [80, 61.5, 2500, 1700, 800, 0.26],
      backgroundColor: ['#77f3c6', '#8ac6ff', '#ffb454', '#c9a8ff', '#7ce0ff', '#f57f9c']
    }
  ],
  source: 'Figures summarized from Reuters, TechCrunch, AP, and company filings (see Research briefing)',
  sourceDate: '2023–2025'
};
