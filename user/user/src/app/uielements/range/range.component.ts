import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { BaseComponentComponent } from '../../base-component/base-component.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CurrentValuesComponent } from '../../current-values/current-values.component';

@Component({
  selector: 'app-range',
  standalone: true,
  imports: [CommonModule, FormsModule, CurrentValuesComponent],
  templateUrl: './range.component.html',
  styleUrl: './range.component.scss'
})
export class RangeComponent extends BaseComponentComponent {

}
