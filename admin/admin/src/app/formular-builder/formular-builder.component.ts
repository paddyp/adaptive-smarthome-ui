import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormioModule } from '@formio/angular';
import { FormlyFieldConfig } from '@ngx-formly/core';


@Component({
  selector: 'app-formular-builder',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, FormioModule,],
  templateUrl: './formular-builder.component.html',
  styleUrl: './formular-builder.component.scss'
})
export class FormularBuilderComponent {
  private _formSchema: any;
  form = new FormGroup({});

  get formSchema() {
    return this._formSchema;
  }

  @Input("schema")
  set formSchema(value: any) {
    this._formSchema = value;
    this.initForm();
  }

  generalForm: FormGroup | undefined;
  constructor(private fb: FormBuilder) { }


  initForm(): void {
    const formGroupConfig: { [key: string]: any } = {};

    // Iteriere durch das Schema und erstelle die Formularsteuerelemente
    for (const key in this.formSchema) {
      if (this.formSchema.hasOwnProperty(key)) {
        const validators = this.getValidators(this.formSchema[key]); // Funktion zum Extrahieren von Validatoren
        formGroupConfig[key] = [null, validators];
      }
    }
    console.log("general form updated")
    this.generalForm = this.fb.group(formGroupConfig);
  }

  getValidators(schemaProperty: any): any[] {
    const validators: any[] = [];
    if (schemaProperty.required) {
      validators.push(Validators.required);
    }
    // Füge weitere Validatoren hinzu, je nach Bedarf (z.B., Validators.email für E-Mail)

    return validators;
  }

  onSubmit(): void {
    if (this.generalForm?.valid) {
      const formData = this.generalForm.value;
      // Hier kannst du die Formulardaten verwenden oder senden
      console.log(formData);
    }
  }

  submit(): void {
    console.log("validate");
  }

}
