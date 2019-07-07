  
  $(document).ready(function() {

    $("#mainForm").submit(function(e) {
        e.preventDefault();


  var uuid = $("#uuid").val()
  
   $(function () {

              $.ajax({
               type: 'GET',
               url: '/people/' + uuid,
               success: function(data) {
                $("#passenger_table").show();
                $("#btn").hide();
                var event_data = '';
                    /*console.log(value);*/
                    event_data += '<tr>';
                    event_data += '<td>'+data.uuid+'</td>';
                    event_data += '<td>'+data.survived+'</td>';
                    event_data += '<td>'+data.age+'</td>';
                    event_data += '<td>'+data.fare+'</td>';
                    event_data += '<td>'+data.sex+'</td>';
                    event_data += '<td>'+data.parentsOrChildrenAboard+'</td>';
                    event_data += '<td>'+data.passengerClass+'</td>';
                    event_data += '<td>'+data.siblingsOrSpousesAboard+'</td>';
                    event_data += '</tr>';
                    
                $("#passenger_table").append(event_data);
             
               //console.log('success', event_data);
               },
               error: function() {
                $("#passenger_table").hide();
                
            }
              });
            });



          });
        })
            