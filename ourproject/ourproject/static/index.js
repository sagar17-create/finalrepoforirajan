fetch("http://127.0.0.1:8000/productview/")  // access JS through serializer
.then((x) => x.json())
.then((x) => console.log(x))
.finally(console.log("Statement Completed"));