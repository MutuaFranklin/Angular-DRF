import { Component, OnInit } from '@angular/core';
import { MainService } from 'src/app/services/main.service';
import { Services } from 'src/app/models/services';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  services!:Services[];

  constructor(private search:MainService) { }

  ngOnInit(): void {
  }

  searchService(input:string){
    if(input){
      console.log(input)
      this.search.searchService(input).toPromise().then((response:any)=>{
        if(response){
          console.log(response)
          this.services = response;
        }
        else{
          alert('Nothing found on ' + input)
        }
      });
    }
  }

}
