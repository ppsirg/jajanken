
function keyInArray(key, response_obj) {
  // check if there is a name in an array of objects
  for (var i = 0; i < response_obj.data.length; i++) {
    if (response_obj.data[i]['name'] === key.toUpperCase()) {
      console.log('found '+key);
      return response_obj.data[i];
  }
}
return null;
}
