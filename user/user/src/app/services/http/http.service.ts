import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  private APIUrl = 'http://fastapi:8000';
  constructor(
    private http: HttpClient,
  ) { }

  private log(message: string) {
    console.log(message);
  }

  getTestAPI(): {} {
    return this.http.get<String>(this.APIUrl)
  }
}
