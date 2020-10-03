import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

@Injectable()
export class BaseUrlInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const url = environment.API_ENDPOINT;
    req = req.clone({
      url: url + req.url
    });
    return next.handle(req);
  }
}

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const userToken = sessionStorage.getItem('token')
    const modifiedReq = req.clone({
      headers: req.headers.set('token', userToken ? userToken : 'invalid'),
    });
    return next.handle(modifiedReq);
  }
}
