import { Routes } from '@angular/router';
import { AuthGuard } from './auth.guard';

import { UserLayoutComponent } from './layouts/user-layout/user-layout.component'
import { LoginComponent } from './pages/login/login.component';

export const AppRoutes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full',
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: '',
    component: UserLayoutComponent,
    canActivate: [AuthGuard],
    children: [
      {
        path: '',
        loadChildren: () => import('src/app/layouts/user-layout/user-layout.module').then(m => m.UserLayoutModule)
      }
    ]
  },
  {
    path: '**',
    redirectTo: 'dashboard'
  }
]
