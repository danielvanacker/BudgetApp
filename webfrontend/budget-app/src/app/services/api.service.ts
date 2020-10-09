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

  public getTransactionMonths(): Observable<any> {
    return this.http.get('transaction/months');
  }

  public getElapsedBudget(): Observable<any> {
    return this.http.get('budget/elapsed');
  }


  public addTransaction(transaction: any): Observable<any> {
    return this.http.post(
      'transactions',
      transaction,
      {
        headers: new HttpHeaders({
          'Content-Type':  'application/json',
          'Accept': 'application/json',
        })
      }
    );
  }

  public addCategory(category: any): Observable<any> {
    return this.http.post(
      'categories',
      category,
      {
        headers: new HttpHeaders({
          'Content-Type':  'application/json',
          'Accept': 'application/json',
        })
      }
    );
  }

  public addPerson(person: any): Observable<any> {
    return this.http.post(
      'people',
      person,
      {
        headers: new HttpHeaders({
          'Content-Type':  'application/json',
          'Accept': 'application/json',
        })
      }
    );
  }

  public addBudget(budget: any): Observable<any> {
    return this.http.post(
      'budget',
      budget,
      {
        headers: new HttpHeaders({
          'Content-Type':  'application/json',
          'Accept': 'application/json',
        })
      }
    );
  }

  public validateUserSession(idToken: string): Observable<any> {
    sessionStorage.setItem('token', idToken);
    return this.http.post(
      'validate_session',
      { token: idToken },
      {
        headers: new HttpHeaders({
          'Content-Type':  'application/json',
          'Accept': 'application/json',
        })
      }
    )
  }

}
