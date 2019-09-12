





axios.get(baseURL+apiURL+'players')
  .then(function (response) {
    // handle success
    console.log(response);
    for (var i = 0; i < response.data.length; i++) {
      console.log(response.data[i]);
    }
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });
