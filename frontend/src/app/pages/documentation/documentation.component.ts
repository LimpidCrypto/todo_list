import { Component } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';
import { OrganismsModule } from '../../shared/components/organisms/organisms.module';

@Component({
  selector: 'documentation-page',
  standalone: true,
  templateUrl: './documentation.component.html',
  styleUrl: './documentation.component.scss',
  imports: [
    SharedModule,
    OrganismsModule,
  ]
})
export class DocumentationPage {

}
