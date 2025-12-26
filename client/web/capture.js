const keystrokes = [];
const mouseMoves = [];

let lastKeyTime = null;
let lastMouseTime = null;

document.getElementById("input").addEventListener("keydown", (e) => {
  const now = performance.now();
  if (lastKeyTime !== null) {
    keystrokes.push({
      flight: now - lastKeyTime
    });
  }
  lastKeyTime = now;
});

document.getElementById("input").addEventListener("keyup", (e) => {
  const now = performance.now();
  keystrokes.push({
    dwell: now - lastKeyTime
  });
});

document.addEventListener("mousemove", (e) => {
  const now = performance.now();
  if (lastMouseTime !== null) {
    mouseMoves.push({
      dx: e.movementX,
      dy: e.movementY,
      dt: now - lastMouseTime
    });
  }
  lastMouseTime = now;
});

function finalize() {
  const features = extractFeatures(keystrokes, mouseMoves);
  document.getElementById("output").textContent =
    JSON.stringify(features, null, 2);
}