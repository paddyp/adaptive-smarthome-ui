import { Component, Input } from '@angular/core';
import { Value } from '../interfaces/uielement';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-current-values',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './current-values.component.html',
  styleUrl: './current-values.component.scss'
})
export class CurrentValuesComponent {
  @Input() values!: [Value]
}
