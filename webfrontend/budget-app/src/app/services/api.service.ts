import { Injectable } from '@angular/core';
import { Observable, throwError, of } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {  }

  public getAllTransactions(): Observable<any> {
    return this.http.get('transactions')
  }

  public getPeople(): Observable<any> {
    return this.http.get('people');
  };

  public getCategories(): Observable<any> {
    return this.http.get('categories');
  };

  public addTransaction(transaction: any): Observable<any> {
    return this.http.post(
      'transaction',
      transaction,
      {
        headers: new HttpHeaders({
          'Content-Type':  'application/json',
          'Accept': 'application/json',
        })
      }
    );
  }
}
