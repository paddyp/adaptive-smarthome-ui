import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Bootstrap5FrameworkModule } from '@zajsf/bootstrap5';
import { CommonModule } from '@angular/common';
import { BasetabComponent } from '../basetab/basetab.component';
@Component({
  selector: 'app-context-of-use-view',
  standalone: true,
  imports: [Bootstrap5FrameworkModule, CommonModule],
  templateUrl: './context-of-use-view.component.html',
  styleUrl: './context-of-use-view.component.scss'
})
export class ContextOfUseViewComponent extends BasetabComponent {
  override BASE_INFORMATION: object = {};
  override createData = JSON.parse(JSON.stringify(this.BASE_INFORMATION)) // copy object
  override type = "contextofuse"
}
