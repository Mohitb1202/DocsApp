import { RouterModule, Routes } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';
import { CustomerComponent } from './customer/customer.component';
import { LoginComponent } from './login/login.component';
import { AuthGuardService } from './docs-services/auth-service/auth-guard.service';
import { RegisterComponent } from './register/register.component';


const routes: Routes = [

  { path: '', component: CustomerComponent,canActivate: [AuthGuardService] },
  { path: 'home', component: CustomerComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },

];
export const routing: ModuleWithProviders<RouterModule> = RouterModule.forRoot(routes);
