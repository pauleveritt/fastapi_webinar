fetch('/heroes/')
  .then(response => response.json())
  .then(data => console.log(data));
