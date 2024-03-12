import { Component } from '@angular/core';
import { BasetabComponent } from '../basetab/basetab.component';
import { ReactiveFormsModule } from '@angular/forms';
import { Bootstrap5FrameworkModule } from '@zajsf/bootstrap5';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-uielement',
  standalone: true,
  imports: [ReactiveFormsModule, Bootstrap5FrameworkModule, CommonModule],
  templateUrl: './uielement.component.html',
  styleUrl: './uielement.component.scss'
})
export class UielementComponent extends BasetabComponent {
  override type = "uielement";


}
