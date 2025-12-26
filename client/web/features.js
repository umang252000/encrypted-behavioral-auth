function mean(arr) {
  return arr.length ? arr.reduce((a, b) => a + b, 0) / arr.length : 0;
}

function variance(arr, m) {
  return arr.length
    ? arr.reduce((a, b) => a + Math.pow(b - m, 2), 0) / arr.length
    : 0;
}

function extractFeatures(keystrokes, mouseMoves) {
  const flights = keystrokes.map(k => k.flight).filter(Boolean);
  const dwells = keystrokes.map(k => k.dwell).filter(Boolean);

  const speeds = mouseMoves.map(m =>
    Math.sqrt(m.dx * m.dx + m.dy * m.dy) / (m.dt || 1)
  );

  return {
    keystroke_flight_mean: mean(flights),
    keystroke_flight_var: variance(flights, mean(flights)),
    keystroke_dwell_mean: mean(dwells),
    mouse_speed_mean: mean(speeds),
    mouse_speed_var: variance(speeds, mean(speeds))
  };
}