import { Routes } from '@angular/router';

import { UserLayoutComponent } from './layouts/user-layout/user-layout.component'

export const AppRoutes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full',
  },
  {
    path: '',
    component: UserLayoutComponent,
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
