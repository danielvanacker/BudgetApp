import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {  }

  public getPeople(): Observable<any> {
    return this.http.get('');
  };

  public getCategories(): Observable<any> {
    return this.http.get('');
  };
}
