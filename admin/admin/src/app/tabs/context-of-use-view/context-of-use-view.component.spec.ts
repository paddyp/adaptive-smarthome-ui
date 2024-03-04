import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContextOfUseViewComponent } from './context-of-use-view.component';

describe('ContextOfUseViewComponent', () => {
  let component: ContextOfUseViewComponent;
  let fixture: ComponentFixture<ContextOfUseViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ContextOfUseViewComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ContextOfUseViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
