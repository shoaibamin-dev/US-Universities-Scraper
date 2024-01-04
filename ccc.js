

let counter = 1;


jobs.forEach((job, i) => {

    var contents = ""

    for (const property in job) {

        if (property.toLowerCase() === "title") {
            contents += `<h4 class="card-title h5 fw-bold mb-4 text-white">${job[property]}</h4>`
        }
        else if (property.toLowerCase() === "name") {
            contents += `<h4 class="card-title h5 fw-bold mb-4 text-white">${job[property]}</h4>`
        }
        else {
            contents += `<p class="card-text mb-1">${property}: <span class="fw-bold">${job[property]}</span></p>`
        }



    }


    $('.korean-jobs-container').append(
        `<div class="col-xl-6 col-md-6">
          <div class="card border-0 dark shadow-sm h-shadow shadow-ts p-3" style="background: linear-gradient(rgba(0,0,0,.9), rgba(0,0,0,.9)), url('images/blocks/preview/card-2/${counter % 4}.jpg') no-repeat top center / cover; letter-spacing: 1px;">
              <div class="card-body">
                  <h6 class="fw-normal text-uppercase ls2 text-white-50 mb-2">NEW</h6>
              
              ${contents}

              <a class="bg-white text-dark" href="https://form.jotform.com/220292740336451" style="
padding: 9px;
padding-left: 28px;
border-radius: 25px;
">Contact<i class="icon-line-arrow-right h4 icon-stacked text-center " style="line-height: 2.25em;"></i></a>
              </div>
          </div>
      </div>
  `)

})	
