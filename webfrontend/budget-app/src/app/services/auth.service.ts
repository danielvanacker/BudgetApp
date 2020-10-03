import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  // inspired and partially coppied from https://github.com/jorgecf/google-oauth-angular
  public gapiSetup: boolean = false; // marks if the gapi library has been loaded
  public authInstance: gapi.auth2.GoogleAuth;
  public error: string;
  public user: gapi.auth2.GoogleUser;

  async ngOnInit() {
    if (await this.getIsLoggedIn()) {
      console.log("getting uer")
      this.user = this.authInstance.currentUser.get();
    }
  }

  async initGoogleAuth(): Promise<void> {
    //  Create a new Promise where the resolve function is the callback
    // passed to gapi.load
    const pload = new Promise((resolve) => {
      gapi.load('auth2', resolve);
    });

    // When the first promise resolves, it means we have gapi loaded
    // and that we can call gapi.init
    return pload.then(async () => {
      await gapi.auth2
        .init({ client_id: environment.CLIENT_ID })
        .then(auth => {
          this.gapiSetup = true;
          this.authInstance = auth;
        });
    });
  }

  // Gets the user idToken
  getUserId(): Observable<any>{
    if(!this.user) {
      this.user = this.authInstance.currentUser.get();
    }
    const idToken: string = this.user.getAuthResponse().id_token;
    return of(idToken);
  }

  async authenticate(): Promise<void> {
    // Initialize gapi if not done yet
    if (!this.gapiSetup) {
      await this.initGoogleAuth();
    }

    // Resolve or reject signin Promise
    await this.authInstance.signIn().then(
      user => this.user = user,
      error => this.error = error
    );
    console.log("Below is user")
    console.log(this.user)
  }

  async logout(): Promise<void> {
    //Initialize gapi if not done
    if(!this.gapiSetup) {
      await this.initGoogleAuth();
    }

    await this.authInstance.signOut();
    sessionStorage.removeItem('token');
  }

  async getIsLoggedIn(): Promise<boolean> {
    // Initialize gapi if not done yet
    if (!this.gapiSetup) {
      await this.initGoogleAuth();
    }

    return this.authInstance.isSignedIn.get();
  }

  getUserProfile(): Observable<any> {
    if(!this.user) {
      this.user = this.authInstance.currentUser.get();
    }
    const profile = this.user.getBasicProfile()
    return of({firstName: profile.getGivenName(),
    lastName: profile.getFamilyName(),
    email: profile.getEmail(),
    imageUrl: profile.getImageUrl()
  })
  }
}
