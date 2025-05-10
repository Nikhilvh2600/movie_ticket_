
    document.addEventListener('DOMContentLoaded', () => {
      const seatElements = document.querySelectorAll('.seat');
      const selectedSeatsInput = document.getElementById('selectedSeatsInput');
      const payButton = document.getElementById('payButton');
    
      let selectedSeatIds = [];
      let totalPrice = 0;

      seatElements.forEach(seat => {
        seat.addEventListener('click', () => {
          const seatId = seat.getAttribute('data-seat-id');
          const price = parseInt(seat.getAttribute('data-price'), 10);
    
          if (seat.classList.contains('selected')) {
            seat.classList.remove('selected');
            selectedSeatIds = selectedSeatIds.filter(id => id !== seatId);
            totalPrice -= price;
          } else {
            seat.classList.add('selected');
            selectedSeatIds.push(seatId);
            totalPrice += price;
          }
    
          selectedSeatsInput.value = selectedSeatIds.join(',');
          payButton.innerText = `Pay Rs.${totalPrice}`;
        });
      });
    });
