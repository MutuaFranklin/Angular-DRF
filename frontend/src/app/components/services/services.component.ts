import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Services } from 'src/app/models/services';
import { MainService } from 'src/app/services/main.service';



@Component({
  selector: 'app-services',
  templateUrl: './services.component.html',
  styleUrls: ['./services.component.css']
})
export class ServicesComponent implements OnInit {

  services!:Services[]


  constructor(
    private http: HttpClient,
    private servicesService: MainService,

  )

  { }

  ngOnInit(){
    let promise = new Promise <void> ((resolve,reject)=>{
      this.servicesService.getAllServices().toPromise().then(
        (response:any) => {
          console.log(response)
        this.services = response;
        resolve()
      },
      (error:string) => {

      })
    })
    return promise


  }

}
