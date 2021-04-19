function myFunction() {
  var currentTimeStamp = new Date(); 
  currentTimeStamp.setDate(currentTimeStamp.getDate() - 1);  
  var currentDate = Utilities.formatDate(currentTimeStamp, "GMT+1", "dd/MM/yyyy")
  
  Logger.log(currentDate);
  
  var filterValues = [currentDate]; // Please set the filter values.
  var column = 5; // In this case, it's the column "C". Please set the column number.
  Logger.log(filterValues);
  
  var ss2 = SpreadsheetApp.getActiveSpreadsheet();
  const sheet_sb2 = ss2.getSheetByName("pivotTable");  
  var sh1 = sheet_sb2.getRange("A:AC");
  sh1.clearContent();

  var  data;
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet_sb = ss.getSheetByName("mainFile");
  let range = sheet_sb.getDataRange();
  var values = range.getValues();
  
  var currentDate2;
  var object = values.reduce(function(o, e, i) {
    var currentDate2 = Utilities.formatDate(new Date(e[column - 1]), "GMT", "dd/MM/yyyy")  
    if (filterValues.indexOf(currentDate2) > -1) 
    {
      Logger.log("selected : "+currentDate2 +" | "+currentDate);
      o.shownRows.push(i + 1);
      st= i+"1";
      o.shownRowValues.push(e);  
    } 
    else 
    {
      o.hiddenRows.push(i + 1);
      o.hiddenRowValues.push(e);
    }
    return o;
  }, {hiddenRows: [], hiddenRowValues: [], shownRows: [], shownRowValues: []});

  // Logger.log(object);
  data = object.shownRowValues;
  //Logger.log(typeof data)
  Logger.log(data);

  var maxrange = sheet_sb2.getActiveRange();
  maxrange.clearContent();
  
  var targetSheeet = sheet_sb2;
  targetSheeet.getRange(2, 1, data.length, data[0].length).setValues(data);
    
  if(range.getFilter() != null){
      range.getFilter().remove();
   }
   range.createFilter();
   
}

