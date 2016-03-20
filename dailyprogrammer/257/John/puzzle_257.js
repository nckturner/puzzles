var fs = require("fs");
var papa = require("./papaparse.js")
var file = fs.readFileSync('../presidents.csv', 'utf8');
var csvToJson = [];
var presidentsRaw = [];
var presidentsObj = [];
var firstPresidentYob = 1732;
var CurrentYear = 2016;
var presidentLifeRangeHashMap = {};

(function tooManyPresidents()
{
	//Initialize hashmap
	for(var x = firstPresidentYob; x <= CurrentYear; x++) {
		presidentLifeRangeHashMap[x] = 0; 
	}

	//Parse .csv file and convert it to JSON
	csvToJson = papa.parse(file);
	var presidentsRaw = csvToJson.data.slice(1);

	//Save JSON objects inton president object
	for(var x = 0; x < presidentsRaw.length; x++){
		var president = {
			fullName : presidentsRaw[x][0],
			birthDate : presidentsRaw[x][1],
			birthPlace : presidentsRaw[x][2],
			deathDate :  presidentsRaw[x][3],
			locationOfDeath : presidentsRaw[x][4]
		};
		presidentsObj.push(president);
	}

	/**
	 * remove excess whitespace in parsed death date.
	 * If dead date is blank, replace it with current date 
	 * since president is stil alive.
	 */
	for(var x = 0; x < presidentsObj.length; x++){
		presidentsObj[x].deathDate = presidentsObj[x].deathDate.trim();
		if( (presidentsObj[x].deathDate.replace(/ /g,'').length) == 0 ){
			presidentsObj[x].deathDate ="Mar 18 2016";
		}
	}

	//For each president, increment the count in the year that
	//they lived.
	for(var x = 0; x < presidentsObj.length; x++) {
		var fromDate = new Date(presidentsObj[x].birthDate).getFullYear();
		var toDate = new Date(presidentsObj[x].deathDate).getFullYear();

		for(var y = fromDate; y <= toDate; y++) {
			presidentLifeRangeHashMap[y] = presidentLifeRangeHashMap[y] + 1;
		}
	}

	var maxCount = findMaxCount(presidentLifeRangeHashMap[firstPresidentYob], presidentLifeRangeHashMap);
	printAnswer(maxCount);

})();

/**
 * Find the max counter (year).
 */
function findMaxCount(currentMax){

	for(var x = firstPresidentYob; x < CurrentYear; x++){
		if(currentMax < presidentLifeRangeHashMap[x]){
			currentMax = presidentLifeRangeHashMap[x];
		}
	}
	return currentMax;
}

/**
 * Find the years that have the max count and print them.
 */
function printAnswer(maxCount){
	console.log('Year\'s with most presidents alive:');
	for(var x = firstPresidentYob; x < CurrentYear; x++){
		if(presidentLifeRangeHashMap[x] == maxCount){
			console.log(x);
		}
	}
}