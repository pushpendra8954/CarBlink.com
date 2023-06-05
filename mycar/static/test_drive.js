var test_drive = {
    authenticate: function () {debugger
        var name = document.getElementById("cust1_name").value;
        var email = document.getElementById("cust1_email").value;
        var mob_no = document.getElementById("cust1_phone").value;
        var ret_book_name = document.getElementById("ret_book_name").value;
        var ret_date = document.getElementById("ret_date").value;
        var flagechk = true;


        if (email == ''){
            flagechk = false;
            return;
        }
        if (name == ''){
            flagechk = false;
            return;
        }
        if (mob_no == ''){
            flagechk = false;
            return;
        }
        if (ret_book_name == ''){
            flagechk = false;
            return;
        }
        if (ret_date == ''){
            flagechk = false;
            return;
        }
        if(flagechk==true){
            alert("YOUR TEST DRIVE IS BOOKED SUCCESSFULLY..");
        }else{
            alert("Something Went Wrong..");
        }
      
        //     } else {

        //     }

        // })
        // .catch(function (response) {
        //     console.log(response);
        // });
    },
    
}