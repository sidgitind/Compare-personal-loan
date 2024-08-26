const addPrepaymentButtons = document.querySelectorAll('.add-prepayment');
const prepaymentContainers = document.querySelectorAll('.prepayments-container');

addPrepaymentButtons.forEach((button, index) => {
  button.addEventListener('click', () => {
    const container = prepaymentContainers[index];
    const year = container.children.length + 1;
    const input = document.createElement('input');
    input.type = 'number';
    input.id = `prepayment${index + 1}_${year}`;
    input.name = `prepayment${index + 1}_${year}`;
    input.placeholder = `Year ${year}`;

    // Check if the input was created successfully
    if (input) {
      container.appendChild(input);
      console.log(`Prepayment input for year ${year} created successfully.`);
    } else {
      console.error('Error creating prepayment input.');
    }
  });
});