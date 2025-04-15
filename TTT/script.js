const board = document.getElementById("board");
const statusDisplay = document.getElementById("status");
const restartButton = document.getElementById("restart");
const toggleAI = document.getElementById("toggleAI");

let cells = [];
let currentPlayer = "X";
let isGameOver = false;
let playWithAI = true;

function initBoard() {
  board.innerHTML = "";
  cells = [];
  isGameOver = false;
  currentPlayer = "X";
  statusDisplay.textContent = "Player X's turn";

  for (let i = 0; i < 9; i++) {
    const cell = document.createElement("div");
    cell.classList.add("cell");
    cell.addEventListener("click", () => handleMove(i));
    board.appendChild(cell);
    cells.push(cell);
  }
}

function handleMove(index) {
  if (isGameOver || cells[index].textContent) return;

  cells[index].textContent = currentPlayer;
  cells[index].classList.add(currentPlayer.toLowerCase());

  if (checkWinner()) {
    statusDisplay.textContent = `Player ${currentPlayer} wins!`;
    isGameOver = true;
    return;
  }

  if (isDraw()) {
    statusDisplay.textContent = "It's a draw!";
    isGameOver = true;
    return;
  }

  currentPlayer = currentPlayer === "X" ? "O" : "X";
  statusDisplay.textContent = `Player ${currentPlayer}'s turn`;

  if (playWithAI && currentPlayer === "O") {
    setTimeout(aiMove, 500); // AI delay
  }
}

function aiMove() {
  if (isGameOver) return;

  let emptyIndices = cells
    .map((cell, index) => cell.textContent === "" ? index : null)
    .filter(i => i !== null);

  if (emptyIndices.length === 0) return;

  const randomIndex = emptyIndices[Math.floor(Math.random() * emptyIndices.length)];
  handleMove(randomIndex);
}

function checkWinner() {
  const wins = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
  ];

  return wins.some(combination => {
    const [a, b, c] = combination;
    return (
      cells[a].textContent &&
      cells[a].textContent === cells[b].textContent &&
      cells[a].textContent === cells[c].textContent
    );
  });
}

function isDraw() {
  return cells.every(cell => cell.textContent !== "");
}

restartButton.addEventListener("click", initBoard);
toggleAI.addEventListener("change", () => {
  playWithAI = toggleAI.checked;
  initBoard();
});

// Initialize game on load
initBoard();
