<<<<<<< HEAD
<<<<<<< HEAD
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }
}
=======
=======
>>>>>>> 6c3af48c2a4d0ae3b4fc657cd5be8d174cf28bf9
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    console.log('log');
    console.error('error');
    console.warn('warn');
    console.debug('debug');
    console.info('info');
    return 'Hello World!';
  }
}
<<<<<<< HEAD
>>>>>>> 6c3af48 (Subiendo todos los archivos desde la nueva computadora)
=======
>>>>>>> 6c3af48c2a4d0ae3b4fc657cd5be8d174cf28bf9
