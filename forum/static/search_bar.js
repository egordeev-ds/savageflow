function handleSearch() {
  const inputElement = document.getElementById('filter-input');
  handleFilterChange(inputElement.value.trim().toLowerCase());
}

function handleFilterChange(filterValue) {
  const questionItems = document.querySelectorAll('.question');

  questionItems.forEach(function(item) {
    const questionTitle = item.querySelector('.question-title');
    const questionContent = item.querySelector('.question-details');

    const questionTitleText = questionTitle.textContent.toLowerCase();
    const questionContentText = questionContent.textContent.toLowerCase();

    if (questionTitleText.includes(filterValue) || questionContentText.includes(filterValue)) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  });
}

const inputElement = document.getElementById('filter-input');
inputElement.addEventListener('input', handleSearch);
