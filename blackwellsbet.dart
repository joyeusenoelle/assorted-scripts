import 'dart:math';

List<String> lm = ["Less","More"];

List getRand(ary) {
  var aryrng = new Random();
  return ary[aryrng.nextInt(ary.length)];
}

num guesses(num tries, num x_max, num y_max, [bool use_d, num d_max]) {
  num successes = 0;
  var rng = new Random();
  String guess = "";
  for (var i = 0; i < tries; i++) {
    var x = rng.nextInt(x_max);
    var y = rng.nextInt(y_max);
    while (x == y) {
      y = rng.nextInt(y_max);
    }
    var lm_loc = (y > x) ? "More" : "Less";
    if (use_d == null) {
      guess = getRand(lm);
    } else {
      var d = rng.nextInt(d_max);
      while (d == x) {
        d = rng.nextInt(d_max);
      }
      guess = (d > x) ? "More" : "Less";
    }
    if (guess == lm_loc) {
      successes += 1;
    }
  }
  return successes;
}

void main(args) {
  num tries, x_max, y_max, d_max;
  try {
    tries = int.parse(args[0]);
    x_max = int.parse(args[1]);
    y_max = int.parse(args[2]);
    d_max = int.parse(args[3]);
  } catch (e) {
    print("Not enough arguments, using defaults");
    tries = 10000;
    x_max = 10000;
    y_max = 10000;
    d_max = 10000;
  }
  print("Starting values: tries $tries, x_max $x_max, y_max $y_max, d_max $d_max");
  num successes_d = guesses(tries, x_max, y_max, true, d_max);
  num successes_n = guesses(tries, x_max, y_max);
  print("Without d: $tries tries, $successes_n successes");
  print("With d: $tries tries, $successes_d successes");
}
