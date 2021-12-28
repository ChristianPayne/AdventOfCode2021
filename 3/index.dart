import 'dart:convert';
import 'dart:io';

void main(List<String> args) {
  List<String> data =
      LineSplitter().convert(new File('./input.txt').readAsStringSync());

  Challenge1(List.from(data));
  print("-----------------------------");
  Challenge2(List.from(data));
}

CountData FindCountOfIndex(int index, List data) {
  int zero = 0;
  int one = 0;

  for (int i = 0; i < data.length; i++) {
    if (data[i][index] == "0") {
      zero++;
    } else {
      one++;
    }
  }
  return new CountData()
    ..mostCommon = "${zero > one ? "0" : "1"}"
    ..ones = one
    ..zeros = zero;
}

class CountData {
  int ones = 0;
  int zeros = 0;
  String mostCommon = "";
}

void Challenge1(data) {
  var gammaRateBinary = "";
  var epsilonRateBinary = "";

  for (int i = 0; i < 12; i++) {
    var result = FindCountOfIndex(i, data);
    gammaRateBinary += result.mostCommon == "0" ? "0" : "1";
    epsilonRateBinary += result.mostCommon == "1" ? "0" : "1";
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

void Challenge2(data) {
  List<String> RemoveDataInList(
      String checkString, int index, List<String> data) {
    data.removeWhere((element) => element[index] == checkString);
    return data;
  }

  int CheckListLength(List list) {
    return list.length;
  }

  var oxygenGenRatingBinary = "";
  var cO2ScrRatingBinary = "";

  // Clone Data
  List<String> oxygenData = List.from(data);

  // oxygenGenRatingBinary
  var binaryTracker = "";
  for (int i = 0; i < 12; i++) {
    if (CheckListLength(oxygenData) == 1) break;
    var result = FindCountOfIndex(i, oxygenData);
    if (result.zeros > result.ones) {
      binaryTracker += "0";
    } else if (result.ones > result.zeros) {
      binaryTracker += "1";
    } else {
      binaryTracker += "1";
    }
    oxygenData = RemoveDataInList(binaryTracker[i], i, oxygenData);
  }
  oxygenGenRatingBinary = oxygenData[0];

  // Reset Data
  oxygenData = List.from(data);
  binaryTracker = "";

  // cO2ScrRatingBinary
  for (int i = 0; i < 12; i++) {
    if (CheckListLength(oxygenData) == 1) break;
    var result = FindCountOfIndex(i, oxygenData);
    if (result.zeros < result.ones) {
      binaryTracker += "0";
    } else if (result.ones < result.zeros) {
      binaryTracker += "1";
    } else {
      binaryTracker += "0";
    }
    oxygenData = RemoveDataInList(binaryTracker[i], i, oxygenData);
  }
  cO2ScrRatingBinary = oxygenData[0];

  var oxygenGenRatingNumber = int.parse(oxygenGenRatingBinary, radix: 2);
  var cO2ScrRatingNumber = int.parse(cO2ScrRatingBinary, radix: 2);

  print("Oxygen Generator Rating Binary: $oxygenGenRatingBinary");
  print("CO2 Scrubber Rating Binary: $cO2ScrRatingBinary");

  print("Oxygen Generator Rating Number: $oxygenGenRatingNumber");
  print("CO2 Scrubber Rating Number: $cO2ScrRatingNumber");

  print(
      "Final number for calculation is ${oxygenGenRatingNumber * cO2ScrRatingNumber}");
}
