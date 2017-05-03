/* This script and many more are available free online at
The JavaScript Source!! http://www.javascriptsource.com
Created by: Michael J. Damato | http://developing.damato.net/ */
// State lists
var states = new Array();

states['Canada'] = new Array('Alberta','British Columbia','Ontario');
states['Mexico'] = new Array('Baja California','Chihuahua','Jalisco');
states['United States'] = new Array('California','Florida','New York');


// City lists
var cities = new Array();

cities['Canada'] = new Array();
cities['Canada']['Alberta']          = new Array('Edmonton','Calgary');
cities['Canada']['British Columbia'] = new Array('Victoria','Vancouver');
cities['Canada']['Ontario']          = new Array('Toronto','Hamilton');

cities['Mexico'] = new Array();
cities['Mexico']['Baja California'] = new Array('Tijauna','Mexicali');
cities['Mexico']['Chihuahua']       = new Array('Ciudad Juárez','Chihuahua');
cities['Mexico']['Jalisco']         = new Array('Guadalajara','Chapala');

cities['United States'] = new Array();
cities['United States']['California'] = new Array('Los Angeles','San Francisco');
cities['United States']['Florida']    = new Array('Miami','Orlando');
cities['United States']['New York']   = new Array('Buffalo','new York');


function setStates() {
  cntrySel = document.getElementById('country');
  stateList = states[cntrySel.value];
  changeSelect('state', stateList, stateList);
  setCities();
}

function setCities() {
  cntrySel = document.getElementById('country');
  stateSel = document.getElementById('state');
  cityList = cities[cntrySel.value][stateSel.value];
  changeSelect('city', cityList, cityList);
}

function changeSelect(fieldID, newOptions, newValues) {
  selectField = document.getElementById(fieldID);
  selectField.options.length = 0;
  for (i=0; i<newOptions.length; i++) {
    selectField.options[selectField.length] = new Option(newOptions[i], newValues[i]);
  }
}

// Multiple onload function created by: Simon Willison
// http://simonwillison.net/2004/May/26/addLoadEvent/
function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      if (oldonload) {
        oldonload();
      }
      func();
    }
  }
}

addLoadEvent(function() {
  setStates();
});
