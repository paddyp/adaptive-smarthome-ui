import { Component, Input } from '@angular/core';
import { Bootstrap5FrameworkModule } from '@zajsf/bootstrap5';
import { BasetabComponent } from '../basetab/basetab.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-adapt-uiview',
  standalone: true,
  imports: [Bootstrap5FrameworkModule, CommonModule],
  templateUrl: './adapt-uiview.component.html',
  styleUrl: './adapt-uiview.component.scss'
})
export class AdaptUIViewComponent extends BasetabComponent {
  override type = "adaptui"
  override BASE_INFORMATION: object = {
    "name": "Beispielname",
    "level": 1,
    "explaination": "Diese Regel ist erstellt worden weil ... ",
    "explaination_level": 1,
    "create_actions": [{
      "metauielement_id": 1
    }],
    "influenced_context_of_use_vars": [
      {
        "contextofuse_id": 1
      }
    ],
    "orconditions": [
      {
        "andconditions": [
          {
            "contextvar_id": 1,
            "operator": "EQUAL",
            "value": "Patrik"
          }
        ]
      }
    ]

  };
  override createData = JSON.parse(JSON.stringify(this.BASE_INFORMATION));
}

