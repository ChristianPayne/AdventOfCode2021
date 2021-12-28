import 'dart:convert';
import 'dart:io';

void main(List<String> args) {
  List<String> data =
      LineSplitter().convert(new File('./input.txt').readAsStringSync());

  var gammaRateBinary = "";
  var epsilonRateBinary = "";

  for (int i = 0; i < 12; i++) {
    var result = FindCountOfIndex(i, data);
    gammaRateBinary += result.gammaRateOutput;
    epsilonRateBinary += result.epsilonRateOutput;
  }
  var gammaRateNumber = int.parse(gammaRateBinary, radix: 2);
  var epsilonRateNumber = int.parse(epsilonRateBinary, radix: 2);

  print("Gamma Rate binary: $gammaRateBinary");
  print("Epsilon Rate binary: $epsilonRateBinary");

  print("Gamma Rate number: $gammaRateNumber");
  print("Epsilon Rate number: $epsilonRateNumber");

  print(
      "Final number for calculation is ${gammaRateNumber * epsilonRateNumber}");
}

class Count {
  int zeroCount = 0;
  int oneCount = 0;
  String gammaRateOutput = "";
  String epsilonRateOutput = "";
}

Count FindCountOfIndex(int index, List data) {
  int zero = 0;
  int one = 0;

  for (int i = 0; i < data.length; i++) {
    if (data[i][index] == "0") {
      zero++;
    } else {
      one++;
    }
  }

  var gammaRateOutput = zero > one ? "0" : "1";
  var epsilonRateOutput = zero > one ? "1" : "0";

  return new Count()
    ..zeroCount = zero
    ..oneCount = one
    ..gammaRateOutput = gammaRateOutput
    ..epsilonRateOutput = epsilonRateOutput;
}
