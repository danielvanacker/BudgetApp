import { Routes } from '@angular/router'
import { DashboardComponent } from 'src/app/pages/dashboard/dashboard.component';
import { CalendarComponent } from 'src/app/pages/calendar/calendar.component';

export const UserLayoutRoutes: Routes = [
  { path: 'dashboard', component: DashboardComponent },
  { path: 'calendar', component: CalendarComponent }
];
