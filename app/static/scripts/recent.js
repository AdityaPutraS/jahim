$.post("/recent",function(res){
  for(var i = 0;i < res['namaBarang'].length;i++){
    $('.isiRecent').append(`<div class="row">
      <div class="col-md-12">
        <h4>`+res['namaBarang'][i]+`</h4>
      </div>
    </div>
    <div class="row">
      <div class="col-md-11">
        <p>instock : `+res['jumlah'][i]+`<span style="float:right!important">`+res['namaHimp'][i]+`</span></p>
      </div>
    </div>
    <hr>`);

  }
},"json");
