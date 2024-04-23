import { Component, ElementRef, Input, ViewChild } from '@angular/core';
import SwaggerUI from 'swagger-ui';

@Component({
  selector: 'api-documentation-organism',
  templateUrl: './api-documentation.component.html',
  styleUrl: './api-documentation.component.scss'
})
export class ApiDocumentationComponent {
  @ViewChild('apiDocumentation', { static: true }) ApiDocumentationElement: ElementRef | undefined
  @Input() apiDocumentation: string = '/assets/openApi/documentation.yaml';

  ngAfterContentInit(): void {
    const ui = SwaggerUI({
      url: this.apiDocumentation,
      domNode: this.ApiDocumentationElement?.nativeElement,
    })
  }
}
