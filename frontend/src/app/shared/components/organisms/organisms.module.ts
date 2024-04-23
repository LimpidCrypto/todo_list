import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiDocumentationComponent } from './api-documentation/api-documentation.component';


@NgModule({
  declarations: [
    ApiDocumentationComponent,
  ],
  imports: [
    CommonModule,
  ],
  exports: [
    ApiDocumentationComponent,
  ]
})
export class OrganismsModule { }
